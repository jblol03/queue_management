import 'package:flutter/material.dart';

class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: const Text("Profile")),
        body: Center(
            child:
                Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          Text('Company Name:'), //Fetch data from API
          Text('Services:'), //Fetch data from API
          Text('Information:'), //Fetch data from API
        ])));
  }
}
