from apscheduler.schedulers.background import BackgroundScheduler
from hackernews.views.story_views import ReadStoryViewset


def start():
    scheduler = BackgroundScheduler()
    story = ReadStoryViewset()
    scheduler.add_job(story.save_items_data, "interval", minutes=5, replace_existing=True)
    scheduler.start()
