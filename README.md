Here's a `README.md` file that you can use for your Django project. This file provides a step-by-step guide on how to set up and run the project on different machines.

```markdown
# Cluster Data API

This is a Django project that provides an API endpoint to retrieve cluster data. The endpoint is accessible at `/cluster` and returns data points related to cluster details.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Django installed (`pip install django`).
- A virtual environment tool (optional but recommended).

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```sh
git clone 
cd project-directory
```

### Step 2: Create and Activate a Virtual Environment (Optional)

It is recommended to create a virtual environment to manage your project dependencies. You can create and activate a virtual environment using the following commands:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install Dependencies

Install the required Python packages using `pip`:

```sh
pip install -r requirements.txt
```

If you don't have a `requirements.txt` file, you can create one by running:

```sh
pip freeze > requirements.txt
```

### Step 4: Configure the Database

Apply the migrations to set up your database:

```sh
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create a Superuser (Optional)

If you want to access the Django admin interface, create a superuser:

```sh
python manage.py createsuperuser
```

Follow the prompts to create the superuser.

### Step 6: Run the Development Server

Start the Django development server:

```sh
python manage.py runserver
```

### Step 7: Access the Application

Open your web browser and navigate to the following URLs:

- Home Page: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Cluster Data API: [http://127.0.0.1:8000/cluster/](http://127.0.0.1:8000/cluster/)
- Admin Interface: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Project Structure

```
myproject/
├── clusters/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── myproject/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
```

## Adding Cluster Data

You can add cluster data via the Django admin interface or using the Django shell.

### Using the Admin Interface

1. Navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
2. Log in with your superuser credentials.
3. Add entries for `ClusterDetails`.

### Using the Django Shell

1. Open the Django shell:

   ```sh
   python manage.py shell
   ```

2. Create and save a `ClusterDetails` object:

   ```python
   from clusters.models import ClusterDetails

   cluster = ClusterDetails(
       cluster_id="123",
       cluster_name="Test Cluster",
       connection_id="conn123",
       user_id="user123",
       region="us-west-2",
       backend_key="backend123",
       cluster_version="1.0",
       disk_size=100,
       min_size=1,
       max_size=10,
       desired_size=5,
       instance_type="t2.medium",
       vpc_name="vpc123",
       vpc_id="vpc-123abc",
       public_subnets=["subnet-123", "subnet-456"],
       private_subnets=["subnet-789", "subnet-101"],
       public_subnet_cidr=["192.168.1.0/24", "192.168.2.0/24"],
       private_subnet_cidr=["192.168.3.0/24", "192.168.4.0/24"],
       domain_names=["example.com", "example.org"],
       cluster_endpoint="endpoint.example.com",
       has_created=True,
       lb_url="http://lb.example.com"
   )
   cluster.save()
   ```

3. Exit the Django shell:

   ```python
   exit()
   ```



