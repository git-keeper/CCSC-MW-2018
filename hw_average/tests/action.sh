SUBMISSION_DIR=$1
FILENAME=hw_average.py
FILEPATH="$SUBMISSION_DIR/$FILENAME"

# make sure the student's file exists
if [ ! -f $FILEPATH ]
then
    echo $FILENAME 'does not exist'
    exit 0
fi

# Copy the student's code to the test directory
cp $FILEPATH .

echo "Below is the output from running my tests against your code."

# Run the tests
pytest .

# Make sure to exit 0!
exit 0
