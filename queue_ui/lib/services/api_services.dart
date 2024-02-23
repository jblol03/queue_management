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
