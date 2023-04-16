#!/bin/bash

echo "Please enter the name of the event:"
read eventName

echo "Please enter the type of challenge:"
read challengeType

echo "Please enter the name of the challenge:"
read challengeName

eventDir="$eventName"
challengeDir="$eventDir/$challengeType/$challengeName"
creationDir="$challengeDir/Creation"
breakdownDir="$challengeDir/BreakDown"

if [ -d "$eventDir" ]; then
  echo "Directory $eventDir already exists. Skipping creation."
else
  echo "Creating directory $eventDir."
  mkdir "$eventDir"
fi

if [ -d "$eventDir/$challengeType" ]; then
  echo "Directory $eventDir/$challengeType already exists. Skipping creation."
else
  echo "Creating directory $eventDir/$challengeType."
  mkdir "$eventDir/$challengeType"
fi

if [ -d "$challengeDir" ]; then
  echo "Directory $challengeDir already exists. Skipping creation."
else
  echo "Creating directory $challengeDir."
  mkdir "$challengeDir"
fi

if [ -d "$creationDir" ]; then
  echo "Directory $creationDir already exists. Skipping creation."
else
  echo "Creating directory $creationDir."
  mkdir "$creationDir"
fi

if [ -d "$breakdownDir" ]; then
  echo "Directory $breakdownDir already exists. Skipping creation."
else
  echo "Creating directory $breakdownDir."
  mkdir "$breakdownDir"
fi

if [ -f "$eventDir/README.md" ]; then
  echo "$eventDir/README.md already exists. Skipping creation."
else
  echo "Creating file $eventDir/README.md."
  echo "# Repository for $eventName" > "$eventDir/README.md"
fi

if [ -f "$creationDir/README.md" ]; then
  echo "$creationDir/README.md already exists. Skipping creation."
else
  echo "Creating file $creationDir/README.md."
  echo "# A Quick explanation of the challenge's creation" > "$creationDir/README.md"
fi

if [ -f "$breakdownDir/README.md" ]; then
  echo "$breakdownDir/README.md already exists. Skipping creation."
else
  echo "Creating file $breakdownDir/README.md."
  echo "# Breaking $eventName" > "$breakdownDir/README.md"
fi
