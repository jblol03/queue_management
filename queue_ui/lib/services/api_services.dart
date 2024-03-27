import 'package:http/http.dart' as http;
import 'dart:convert';

class AuthService {
  final String apiUrl = 'http://127.0.0.1:8000';

  Future<bool> login(String email, String password) async {
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

  Future<bool> user_login(String email, String otp) async {
    // Check if OTP is blank
    if (otp == null || otp.trim().isEmpty) {
      // Handle empty OTP field
      return false;
    }

    // Continue with login if OTP is not blank
    final response = await http.post(
      Uri.parse('$apiUrl/api/user/enduser_login/'),
      body: {'email': email, 'otp': otp},
    );

    if (response.statusCode == 200) {
      return true;
    } else {
      // Handle Login Failure
      return false;
    }
  }
}

class DetailsService {
  final String apiUrl = 'http://127.0.0.1:8000';

  Future<Map<String, dynamic>> getDetails() async {
    final response = await http.get(Uri.parse('$apiUrl/details/'));

    if (response.statusCode == 200) {
      // If the server returns a 200 OK response, then parse the JSON.
      return jsonDecode(response.body);
    } else {
      // If the server returns an unsuccessful response code, then throw an exception.
      throw Exception('Failed to load details');
    }
  }
}

class Booking {
  final String apiUrl = 'http://127.0.0.1:8000';
  Future<List> fetchBookings() async {
    final response =
        await http.get(Uri.parse('$apiUrl/api/appointment/bookings/'));

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Failed to load bookings');
    }
  }
}
