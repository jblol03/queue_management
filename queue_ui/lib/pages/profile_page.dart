import 'package:flutter/material.dart';
import 'package:queue_ui/pages/schedule.dart';

class ProfilePage extends StatelessWidget {
  const ProfilePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(title: const Text("Profile")),
        body: Center(
            child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Company Name:'), //Fetch data from API
            const Text('Services:'), //Fetch data from API
            const Text('Information:'), //Fetch data from API

            ElevatedButton(
              child: const Text('Add Schedule'),
              onPressed: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (context) => const Schedule()));
              },
            ),
          ],
        )));
  }
}
