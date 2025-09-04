from rest_framework import serializers
from .models import School, Teacher, Student

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', 'address']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("School name cannot be empty.")
        return value

    def validate_address(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Address must be at least 10 characters long.")
        return value

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'name', 'subject']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Teacher name cannot be empty.")
        return value

    def validate_subject(self, value):
        if not value.strip():
            raise serializers.ValidationError("Subject cannot be empty.")
        return value

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'grade', 'school']
        
    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Student name cannot be empty.")
        return value

    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age cannot be negative.")
        return value

    def validate_grade(self, value):
        if not value.strip():
            raise serializers.ValidationError("Grade cannot be empty.")
        return value
