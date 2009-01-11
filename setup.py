#coding: utf-8
import datetime

from django.db.models import signals
from django.contrib.auth.models import Group, User


from stigull_profile.models import STIGULL_GROUP, GOVERNMENT_GROUP
from events.models import Event, RegistrationValidator, validator_registry
from user_profile.models import controller
from htmlcalendar.classes import event_manager, CalendarEvent

ProfileModel = controller.get_profile_model()

class StigullAttendValidator(RegistrationValidator):
    """ Validates that only logged in users who are members of Stigull can attend events """
    def can_attend(self, user):
        return super(StigullAttendValidator, self).can_attend(user) and user.groups.filter(name = STIGULL_GROUP).count() > 0

validator_registry.add_validator(StigullAttendValidator())


def add_government_to_events(sender, instance, created, **kwargs):
    government_group = Group.objects.get(name = GOVERNMENT_GROUP)

    for user in government_group.user_set.all():
        if not instance.user_is_attending(user):
            instance.add_user_to_list_of_attendees(user)

signals.post_save.connect(add_government_to_events, sender = Event)


def get_birthdays(date):
    kennitala = date.strftime("%d%m")
    profiles = ProfileModel.objects.filter(kennitala__startswith = kennitala)
    events = []
    for profile in profiles:
        name = "%s (%d)" % (profile.get_short_fullname(), profile.get_age_in_years(today = date))
        events.append(CalendarEvent(u"Afmæli", name, profile.get_absolute_url()))
    return events

def get_events(date):
    events = Event.objects.get_events_for_day(date)
    calendar_events = []
    for event in events:
        name = "%s, %s" % (event.name, event.get_duration(date))
        calendar_events.append(CalendarEvent(event.event_type, name, event.get_absolute_url(), event.location))

    return calendar_events

event_manager.register_callback(get_events)
event_manager.register_callback(get_birthdays)