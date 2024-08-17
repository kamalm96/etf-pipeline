# from apscheduler.schedulers.blocking import BlockingScheduler
# from run_etl import main

# scheduler = BlockingScheduler()

# # Schedule ETL to run every hour
# scheduler.add_job(main, "interval", hours=1)

# try:
#     scheduler.start()
# except (KeyboardInterrupt, SystemExit):
#     pass
