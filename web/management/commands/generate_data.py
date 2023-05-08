from datetime import timedelta
from random import randint

from django.core.management.base import BaseCommand
from django.utils.timezone import now

from web.models import Blog, User, BlogTag


class Command(BaseCommand):
    def handle(self, *args, **options):
        current_date = now()
        user = User.objects.first()
        tags = BlogTag.objects.filter()

        blogs = []

        for day_index in range(30):
            current_date -= timedelta(days=1)

            for blog_index in range(randint(5, 10)):
                publication_date = current_date + timedelta(hours=randint(0, 10))

                blogs.append(Blog(
                    title=f'generated title {day_index}-{blog_index}',
                    short_description=f'generated short description {day_index}',
                    description=f'generated description {blog_index}',
                    publication_date=publication_date,
                    user=user
                ))

        saved_blogs = Blog.objects.bulk_create(blogs)

        blog_tags = []
        for blog in saved_blogs:
            count_of_tags = randint(0, len(tags))
            for tag_index in range(count_of_tags):
                blog_tags.append(
                    Blog.tags.through(blog_id=blog.id, blogtag_id=tags[tag_index].id)
                )
        Blog.tags.through.objects.bulk_create(blog_tags)
