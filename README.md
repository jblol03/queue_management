# Queue Management System
The README includes code snippets for cloning the repositories and running the necessary commands for Django and Flutter.

### queue_management (Django Backend)

#### Project Overview:

`queue_management` is a Django-based backend for a queue management system.

#### Getting Started:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/pritam-ravani/queue.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd queue/queue_management
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the API:**

   The API will be available at `http://127.0.0.1:8000/`.

#### Additional Commands:

- **Create a Superuser (Admin):**

    ```bash
    python manage.py createsuperuser
    ```

- **Run Tests:**

    ```bash
    python manage.py test
    ```

### queue_ui (Flutter Frontend)

#### Project Overview:

`queue_ui` is a Flutter-based frontend for the queue management system.

#### Getting Started:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/queue_ui.git
    ```

2. **Navigate to the Project Directory:**

    ```bash
    cd queue_ui
    ```

3. **Install Dependencies:**

    ```bash
    flutter pub get
    ```

4. **Run the App:**

    ```bash
    flutter run
    ```

5. **Access the App:**

   The Flutter app will start on an emulator or connected device.

#### Additional Commands:

- **Build Release APK:**

    ```bash
    flutter build apk --release
    ```

- **Run Tests:**

    ```bash
    flutter test
    ```

### Notes:

- Make sure you have Python, Django, and Flutter installed on your machine.
- Adjust the clone URLs based on your repository locations.
