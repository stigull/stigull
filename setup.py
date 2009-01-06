#coding: utf-8

from django.db.models import signals
from django.contrib.auth.models import Group


from stigull_profile.models import STIGULL_GROUP, GOVERNMENT_GROUP
from events.models import Event, RegistrationValidator, validator_registry



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
