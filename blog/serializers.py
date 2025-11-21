from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    # نمایش کامل اطلاعات category
    category = CategorySerializer(read_only=True)
    # دریافت category با id
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), write_only=True, source='category'
    )

    class Meta:
        model = Post
        fields = "__all__"  # همه فیلدهای Post
        extra_fields = ['category_id']  # فیلد اضافه برای write_only

    def create(self, validated_data):
        # category به طور خودکار از category_id استخراج می‌شود
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
