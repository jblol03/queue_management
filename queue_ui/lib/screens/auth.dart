import 'package:flutter/material.dart';
import 'package:queue_ui/screens/business/business_dashboard.dart';
import 'package:queue_ui/services/api_services.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Login Page',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const LoginPage(),
    );
  }
}

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final AuthService authService = AuthService();
  final TextEditingController _businessEmailController =
      TextEditingController();
  final TextEditingController _businessPasswordController =
      TextEditingController();
  final TextEditingController _userEmailController = TextEditingController();
  final TextEditingController _otpController = TextEditingController();
  bool _isBusiness = true;

  @override
  Widget build(BuildContext context) {
    final double pixelRatio = MediaQuery.of(context).devicePixelRatio;
    final double width = 3.92 * pixelRatio * 160;
    final double height = 2.2 * pixelRatio * 160;

    return Scaffold(
      appBar: AppBar(
        title: const Text('Login Page'),
      ),
      body: Center(
        child: ConstrainedBox(
          constraints: BoxConstraints(
            minWidth: width,
            minHeight: height,
            maxWidth: width,
            maxHeight: height,
          ),
          child: Card(
            margin: const EdgeInsets.all(16.0),
            child: Padding(
              padding: const EdgeInsets.all(16.0),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: <Widget>[
                  Row(
                    children: <Widget>[
                      Expanded(
                        child: TextButton(
                          child: const Text('Business'),
                          onPressed: () {
                            setState(() {
                              _isBusiness = true;
                            });
                          },
                        ),
                      ),
                      Expanded(
                        child: TextButton(
                          child: const Text('User'),
                          onPressed: () {
                            setState(() {
                              _isBusiness = false;
                            });
                          },
                        ),
                      ),
                    ],
                  ),
                  _isBusiness ? businessSection() : userSection(),
                ],
              ),
            ),
          ),
        ),
      ),
    );
  }

  Widget businessSection() {
    return Column(
      children: <Widget>[
        TextField(
          controller: _businessEmailController,
          decoration: const InputDecoration(
            labelText: 'Email',
          ),
        ),
        TextField(
          controller: _businessPasswordController,
          decoration: const InputDecoration(
            labelText: 'Password',
          ),
          obscureText: true,
        ),
        ElevatedButton(
          onPressed: () async {
            //Call API Login
            bool success = await authService.login(
                _businessEmailController.text,
                _businessPasswordController.text);

            if (success) {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const DashboardPage()),
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
      ],
    );
  }

  Widget userSection() {
    return Column(
      children: <Widget>[
        TextField(
          controller: _userEmailController,
          decoration: const InputDecoration(
            labelText: 'Email',
          ),
        ),
        ElevatedButton(
          child: const Text('Send OTP'),
          onPressed: () {
            print('Send OTP button pressed');
          },
        ),
        TextField(
          controller: _otpController,
          decoration: const InputDecoration(
            labelText: 'OTP',
          ),
        ),
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceAround,
          children: [
            ElevatedButton(
              child: const Text('Submit OTP'),
              onPressed: () {
                print('Submit OTP button pressed');
              },
            ),
            TextButton(
              child: const Text('Resend OTP'),
              onPressed: () {
                print('Resend OTP button pressed');
              },
            ),
          ],
        ),
      ],
    );
  }
}
