#! /bin/sh
# wait for mysql to be running
while ! nc -z mysql 3306; do
	echo "waiting for db..."
	sleep 2
done
# make sure the tables exist
python3 create.py
# populate the db if required
echo "DB ENTRY: ${DB_ENTRY}"
if [ "${DB_ENTRY}" = true ]; then
	python3 database_entry.py
fi
if [ "${DB_ENTRY}" = True ]; then
        python3 database_entry.py
fi
# run the application
python3 run.py
