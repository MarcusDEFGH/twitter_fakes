from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from tags.models import Tag
from users.models import User
from users.serializers import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    potential_fake_users = SerializerMethodField()
    reported_users = SerializerMethodField()
    banned_users = SerializerMethodField()

    class Meta:
        model = Tag
        read_only_fields = ('name', 'is_active', 'potential_fake_users',
                            'fake_users', 'fake_users', 'reported_users',
                            'banned_users')

    def get_users(self):
        return User.objects.filter(tag_id=self.id)

    def get_potential_fake_users(self):
        return self.users.filter(potential_fake=True)

    def get_fake_users(self):
        return self.users.filter(is_fake=True)

    def get_reported_users(self):
        return self.users.filter(reported=True)

    def get_banned_users(self):
        return self.users.filter(banned=True)
