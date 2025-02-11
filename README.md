# How to Automate Recurring Scraping Jobs With Scheduler

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/product-integrations/refs/heads/master/Affiliate-Universal-1090x275.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

[<u>Scheduler</u>](https://oxylabs.io/features/scheduler), an add-on to Oxylabs Scraper APIs, allows you to automate recurring scraping and parsing jobs by creating schedules. The main purpose – avoiding tedious repetition and saving time.

The scheduling intervals, ranging from minutes to days, eliminate the need for sending new requests with the same parameters. If you intend to create a periodic task, create a payload once, schedule the job, and Scheduler will take care of the recurrence.

Based on your input, Scheduler:

- Automates recurring requests with the specified frequency.
- Creates multiple schedules for different jobs.
- Uploads data to a cloud storage bucket.
- Notifies once a job is done.

## How does Scheduler work?

To create a schedule, define three points:

1. Submit a **cron schedule expression** to specify the frequency of repetition.
2. Pass a set of **job parameters** to execute at scheduled times.
3. Submit an **end time** to indicate when to stop.

## Job setup

The following is a quick overview of what to expect when working with Scheduler. You can find all the endpoints, parameters, and values with in-depth explanations in our [<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/scheduler).

### Endpoints

You can use endpoints to communicate with our APIs. Scheduler has a number of [<u>endpoints</u>](https://developers.oxylabs.io/scraper-apis/scheduler#endpoints) you can use to control the process:

- Create a new schedule.
- Get a list of your schedules.
- Check information about a specific schedule.
- Deactivate or reactivate a schedule.

### Job parameters

You can provide a set of parameters to be executed as part of a schedule. The parameters depend on a scraping target. Make sure to refer to the documentation of the specific scraper ([<u>Google</u>](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/google), [<u>Amazon</u>](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon), etc.).

### Communication methods

To interact with Oxylabs’ APIs, you can either use an API client, such as Postman, or a preferred programming language that supports HTTP requests. 

For the process of scheduling a job with Postman, check this [<u>video</u>](https://www.youtube.com/watch?v=HJLkFZ_9Z5w).

For the Python tutorial covering all functions of Scheduler, see the following section. 

## Automating a job using Amazon Scraper API and Python

Before continuing, let's review how to fetch product information from Amazon using [<u>Amazon Scraper API</u>](https://oxylabs.io/products/scraper-api/ecommerce/amazon).

The typical code to fetch products from Amazon Scraper API is as follows:

```python
import requests


payload = {
    "source": "amazon_product",  # returns product information
    "query": "B098FKXT8L", # ASIN
    "parse": True,
}


response = requests.post(
    "https://realtime.oxylabs.io/v1/queries",
    auth=("USERNAME", "PASSWORD"),
    json=payload,
)


print(response.json())
```

To learn more about scraping Amazon product data, see our [<u>blog post</u>](https://oxylabs.io/blog/how-to-scrape-amazon-product-data) and review the [<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon).

This guide will showcase how to create schedules instead of calling the API  directly.

## Creating a schedule

You’ll need the following information to create a schedule:

- The API endpoint.
- Your username and password.
- A payload with parameters.

The API endpoint to create schedules: `https://data.oxylabs.io/v1/schedules`. 

You’ll get your username and password when you sign up for a Scraper API. 

Send your username and password as a basic authorization header. You can create an authorization token using the base64 Python package or online tools. 

For example, the string `sampleuser:samplepwd`, when translated to the base64 string, is `c2FtcGxldXNlcjpzYW1wbGVwd2Q=`.

Use this string to construct the Authorization header and send it with the header’s parameters: `"Authorization": "Basic c2FtcGxldXNlcjpzYW1wbGVwd2Q="`.

To create schedules using the API endpoint, send a POST request, including the following (mandatory) parameters in the request body:

- `cron`
- `items`
- `end_time`

### `cron`

The first parameter, `cron`, determines how often your schedule is repeated. The syntax is the same as a standard cron schedule expression.

For example, to schedule your job to run at 4 pm every day, the expression is as follows: `0 16 * * *`.

To learn more about cron schedule expressions, visit [<u>this site</u>](https://crontab.guru/).

### `items`

The second parameter, `items`, is a list of job parameters you want to execute as part of this schedule.

The items in this list are the payload you would send to the API:

```python
{"source": "amazon_product", "query": "B098FKXT8L", "parse": True}
```

Send the same payload as `items` to Scheduler. For more information about the possible job parameter values, see our [<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/e-commerce-scraper-api/amazon).

### `end_time`

The third parameter, `end_time`, determines when the scheduled job stops running. For example, to stop the job on the 1st of January, 2032, at 4 pm, the `end_time` parameter value would be as follows: `"2032-12-01 16:00:00"`.

The following is a JSON that uses values from the examples above:

```python
{
    "cron": "0 16 * * *",
    "items": [
        {
            "source": "amazon_product",
            "query": "B098FKXT8L",
            "parse": True,
        }
    ],
    "end_time": "2032-01-01 16:00:00",
}
)
```

Putting everything together, the Python code to create a schedule is as follows:

```python
import requests
import json


API_URL = "https://data.oxylabs.io/v1/schedules"


payload = json.dumps(
    {
        "cron": "0 16 * * *",
        "items": [
            {
                "source": "amazon_product",
                "query": "B098FKXT8L",
                "parse": True,
            }
        ],
        "end_time": "2032-12-01 16:00:00",
    }
)
headers = {
    "content-type": "application/json",
    "Authorization": "Basic c2FtcGxldXNlcjpzYW1wbGVwd2Q=",
}


response = requests.post(API_URL, headers=headers, data=payload)


print(response.text)
```

If you run this file, you’ll see the following message:

```python
{
    "schedule_id": 3809594044634907291,
    "active": true,
    "items_count": 1,
    "cron": "0 16 * * *",
    "end_time": "2032-12-01 16:00:00",
    "next_run_at": "2023-04-05 16:00:00",
    # more info
}
```

Here you can see the schedule ID. You can use the schedule ID to check the status or to disable the schedule.

Now, let’s capture the output of this schedule using callbacks and cloud storage. 

## Schedules with callbacks and cloud storage

You can use a callback URL that receives the output when a scheduled job executes. Amazon Scraper API sends a POST request to this callback when scraping is complete.

You can also upload your results to cloud storage – Amazon S3 or Google Cloud Storage (GCS).

**NOTE**: it’s convenient to use Scheduler with the upload to cloud storage feature to receive regular data updates without trying to fetch results from our system.

To use GCS, send `storage_type` as `gcs` and set `storage_url` as your GCS bucket name.

To use S3, send `storage_type` as `s3` and set the `storage_url` as your S3 bucket URL.

The following example shows how to use a callback URL with S3:

```python
{
    "cron": "0 16 * * *",
    "items": [
        {
            "source": "amazon",
            "url": "https://www.amazon.com/dp/B098FKXT8L",
            "callback_url": "https://callback.site/path",
            "storage_type": "s3",
            "storage_url": "s3://yourown.s3.bucket/path",
        }
    ],
    "end_time": "2032-12-01 16:00:00",
}
```

## Getting schedule information

When you create a schedule, the output contains `schedule_id`. This ID is a number similar to `1234567890987654321`.

You can send a GET request to `https://data.oxylabs.io/v1/schedules/{id}` to get the details of a schedule:

```python
import requests


schedule_id = "1234567890987654321"
url = "https://data.oxylabs.io/v1/schedules/{id}"


headers = {"Authorization": "Basic c2FtcGxldXNlcjpzYW1wbGVwd2Q="}
response = requests.get(url, headers=headers)
print(response.text)
```

If you run this file, the output will be as follows:

```python
{
    "schedule_id": 1234567890987654321,
    "active": true,
    "items_count": 1,
    "cron": "0 16 * * *",
    "end_time": "2032-12-01 16:00:00",
    "next_run_at": "2023-12-02 16:00:00",
    "stats": {
        "total_job_count": 8,
        "job_create_outcomes": [{"status_code": 202, "job_count": 8, "ratio": 1}],
        "job_result_outcomes": [{"status": "done", "job_count": 8, "ratio": 1}],
    },
}
```

Here is some of the key information in this output:

- `active: true` – the schedule is active.
- `total_job_count` – the total number of items in this schedule.
- `job_create_outcomes` – stats related to job creation.
- `job_result_outcomes` – an outcome for the scraping and parsing jobs performed as part of this schedule.

For more details, see the [<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/scheduler#get-schedule-information). 

If you want to get a list of all schedules, you can send a GET request to the following API endpoint: `https://data.oxylabs.io/v1/schedules`.

It’ll return a list of IDs for all schedules.

## Deactivating or reactivating a schedule

Notice how the schedule information API endpoint returns the schedule status in the `active` field.

You can use the API endpoint, `https://data.oxylabs.io/v1/schedules/{schedule_id}/state`, to activate or deactivate a schedule.

Note that this is a PUT request.

```python
schedule_id = "1234567890987654321"
API_URL = f"https://data.oxylabs.io/v1/schedules/{schedule_id}/state"


payload = json.dumps({"active": False})
headers = {
    "content-type": "application/json",
    "Authorization": "Basic c2FtcGxldXNlcjpzYW1wbGVwd2Q=",
}


response = requests.put(API_URL, headers=headers, data=payload)
```

A successful API call returns the HTTP status code `202` with an empty response.

If you wish to activate this schedule later, use the same API call but send `active` as true:

```python
payload = json.dumps({"active": True})
```

## Wrapping up

You can try Scheduler’s functionality with a one-week free trial of our [<u>Scraper APIs</u>](https://oxylabs.io/products/scraper-api).

Be cautious about the service bills when setting extensive schedules. Make sure to test a job with a few items and limited repeats to ensure you get the expected result. Once verified, stop the test schedule and create a new, scaled-up schedule. 

If you have questions about the process, contact us at support@oxylabs.io or via the live chat on our [<u>homepage</u>](https://oxylabs.io/).
