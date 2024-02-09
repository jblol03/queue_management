import 'package:flutter/material.dart';

class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: const Text("Profile")),
        body: const Center(
            child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text('Company Name:'), //Fetch data from API
            Text('Services:'), //Fetch data from API
            Text('Information:'), //Fetch data from API
            ElevatedButton(
              onPressed: () {
                //Navigate to add schedule page
              },
              child: Text('Add Schedule'),
            ),
          ],
        )));
  }
}
