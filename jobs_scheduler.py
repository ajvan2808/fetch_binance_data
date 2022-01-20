from crontab import CronTab

with CronTab(user='root') as cron:
    job = cron.new(command='fetch_data.py')

    for job in cron:
        job.minute.every(1)
        cron.write('output.tab')
        print(job)
