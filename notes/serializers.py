from rest_framework import serializers
from .models import Note, Tag, Task

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class NoteSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )

    tag_names = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'tags', 'tag_names', 'created_at', 'updated_at']

    def get_tag_names(self, obj):
        return [tag.name for tag in obj.tags.all()]
    

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        note = Note.objects.create(**validated_data)

        for tag_name in tags:
            tag_ob, _ = Tag.objects.get_or_create(name=tag_name)
            note.tags.add(tag_ob)

        return note
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
