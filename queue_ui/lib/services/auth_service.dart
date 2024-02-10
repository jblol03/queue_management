import 'package:http/http.dart' as http;

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
