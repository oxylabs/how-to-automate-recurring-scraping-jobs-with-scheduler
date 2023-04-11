# How to Automate Recurring Scraping Jobs With Scheduler

[<u>Scheduler</u>](https://oxylabs.io/features/scheduler), an add-on to Oxylabs Scraper APIs, allows you to automate recurring scraping and parsing jobs by creating schedules. The main purpose – avoiding tedious repetition and saving time.

The scheduling intervals, ranging from minutes to days, eliminate the need for sending new requests with the same parameters. If you intend to create a periodic task, create a payload once, schedule the job, and Scheduler will take care of the recurrence.

Based on your input, Scheduler:

- Automates recurring requests with the specified frequency.
- Creates multiple schedules for different jobs.
- Uploads data to a cloud storage bucket.
- Notifies once a job is done.

## How does Scheduler work?

To create a schedule, define three points:

1. Submit a cron schedule expression to specify the frequency of repetition.
2. Pass a set of job parameters to execute at scheduled times.
3. Submit an end time to indicate when to stop.

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

The API endpoint to create schedules: https://data.oxylabs.io/v1/schedules. 

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















