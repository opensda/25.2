from rest_framework import serializers

from education.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    # Выводим поле уроков, которые есть на курсе
    def get_lessons(self, course):
        return [lesson.name for lesson in course.lesson.all()]

    # Выводим количество уроков в курсе
    def get_lessons_count(self, course):
        return course.lesson.count()

    def get_subscription(self, course):
        # Выводим данные о статусе подписки на курс

        return [
            subscription.is_subscribed for subscription in course.subscription.all()
        ]
