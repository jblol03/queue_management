import 'package:http/http.dart' as http;
import 'dart:convert';

class AuthService {
  final String apiUrl = 'http://127.0.0.1:8000';

  Future<bool> login(String email, String password) async {
    // Implement login API call
    // Return true if login is successful, false otherwise
    final response = await http.post(
      Uri.parse('$apiUrl/api/user/login/'),
      body: {'email': email, 'password': password},
    );

    if (response.statusCode == 200) {
      return true;
    } else {
      //Handle Login Failure
      return false;
    }
  }

  // Future<bool> register(String username, String password) async {
  //   // Implement register API call
  //   // Return true if registration is successful, false otherwise
  //   return true;
  // }
}

class ProfileService {
  final String apiUrl = 'http://127.0.0.1:8000';

  Future<bool> login(String email, String password) async {
    // Implement login API call
    // Return true if login is successful, false otherwise
    final response = await http.post(
      Uri.parse('$apiUrl/api/user/login/'),
      body: {'email': email, 'password': password},
    );

    if (response.statusCode == 200) {
      return true;
    } else {
      //Handle Login Failure
      return false;
    }
  }
}

class ScheduleService {
  final String apiUrl = 'http://127.0.0.1:8000';

  Future<bool> createSchedule(String title, DateTime date) async {
    // Implement create schedule API call
    // Return true if schedule creation is successful, false otherwise
    final response = await http.post(
      Uri.parse('$apiUrl/api/schedule/create/'),
      body: {'title': title, 'date': date.toIso8601String()},
    );

    if (response.statusCode == 200) {
      return true;
    } else {
      //Handle schedule creation failure
      return false;
    }
  }

  Future<List<Map<String, dynamic>>> getSchedules() async {
    // Implement get schedules API call
    // Return a list of schedules if successful, empty list otherwise
    final response = await http.get(
      Uri.parse('$apiUrl/api/schedule/'),
    );

    if (response.statusCode == 200) {
      // Parse the response body as a list of maps
      List<Map<String, dynamic>> schedules =
          List<Map<String, dynamic>>.from(jsonDecode(response.body));
      return schedules;
    } else {
      //Handle get schedules failure
      return [];
    }
  }
}
