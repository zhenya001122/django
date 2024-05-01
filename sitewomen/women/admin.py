from django.contrib import admin, messages
from .models import Women, Category


class MarriedFilter(admin.SimpleListFilter):
    title = 'Статус женщи'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('married', 'Замужем'),
            ('single', 'Не замужем')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Women)
class AdminWomen(admin.ModelAdmin):
    fields = ['title', 'content', 'slug', 'cat', 'husband', 'tags']
    filter_horizontal = ['tags']
    readonly_fields = ['slug']
    list_display = ('title', 'time_create', 'is_published', 'cat', 'brief_info')
    list_display_links = ('title', )
    ordering = ['-time_create', 'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = [MarriedFilter, 'cat__name', 'is_published']

    @admin.display(description='Краткое описание')
    def brief_info(self, women: Women):
        """создает доп поле (не в БД) в отображении модели в админке"""
        return f"Описание {len(women.content)} символов"

    @admin.action(description='Опубликовать выбранные записи')
    def set_published(self, request, queryset):
        """действия с выбранными записями в админке. Мегяет статус публикации на опубликовано"""
        count = queryset.update(is_published=Women.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description='Снять с публикации выбранные записи')
    def set_draft(self, request, queryset):
        """действия с выбранными записями в админке. Мегяет статус публикации на черновик"""
        count = queryset.update(is_published=Women.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации", messages.WARNING)


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
