## Problem Statement

When users post an update on social media, such as a URL, image, status update, etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e., how many hours, minutes, or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing.

You are given two timestamps of one such post as seen by a user. Your task is to print the absolute difference between them in seconds.

## Timestamp format:

Day dd Mon yyyy hh:mm:ss +xxxx


Here, +xxxx represents the time zone offset.

## Input Format

The first line contains an integer, t, the number of test cases.

Each test case contains two lines, representing timestamps t1 and t2.

## Constraints

Input contains only valid timestamps.

## Output Format

Print the absolute difference between the two timestamps in seconds.

## Sample Input
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

## Sample Output
25200
88200