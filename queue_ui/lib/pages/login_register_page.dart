import 'package:flutter/material.dart';
import 'package:queue_ui/pages/profile_page.dart';
import 'package:queue_ui/services/api_services.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final AuthService authService = AuthService();
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Login")),
      body: Center(
          child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
        TextField(
          controller: emailController,
          decoration: const InputDecoration(labelText: "Email"),
        ),
        TextField(
          controller: passwordController,
          decoration: const InputDecoration(labelText: "Password"),
          obscureText: true,
        ),
        const SizedBox(
          height: 16,
        ),
        ElevatedButton(
          onPressed: () async {
            //Call API Login
            bool success = await authService.login(
                emailController.text, passwordController.text);

            if (success) {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const ProfilePage()),
              );
            } else {
              //Handle Login Failure
              ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
                content: Text("Login Failed. Please try again."),
              ));
            }
          },
          child: const Text("Login"),
        ),
      ])),
    );
  }
}
