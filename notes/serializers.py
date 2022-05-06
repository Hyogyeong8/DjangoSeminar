from rest_framework import serializers
from .models import Note, User, Comment, Course
from datetime import datetime, timedelta, date

# class NoteSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#
#     def create(self, validated_data):
#         return Note.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.content = validated_data.get('content', instance.content)
#         instance.save()
#         return instance

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'parent_course', 'created_by', 'title', 'content', 'comment_count']

    comment_count = serializers.SerializerMethodField(
        read_only = True
    )

    def get_comment_count(self, obj):
        # return Comment.objects.filter(parent_note == obj.id).count()
        return obj.comments.count()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname', 'email']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'number', 'title', 'note_count']

    note_count = serializers.SerializerMethodField(
        read_only=True
    )

    def get_note_count(self, obj):
        start_data = date.today() - timedelta(days=365)
        filter_notes = obj.notes.filter(created__gte=start_data)
        return filter_notes.count()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'created_by', 'parent_note', 'content']


