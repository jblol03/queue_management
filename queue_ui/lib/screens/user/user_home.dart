import 'package:flutter/material.dart';
import '';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Queue Management System'),
        actions: <Widget>[
          IconButton(
            icon: const Icon(Icons.account_circle),
            onPressed: () {
              // Navigate to user profile
            },
          ),
        ],
      ),
      body: const Center(
        child: Text('Home Page'),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: 'Home',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.search),
            label: 'Explore',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.notifications),
            label: 'Notifications',
          ),
        ],
        onTap: (index) {
          // Handle navigation
          switch (index) {
            case 0:
              // Navigate to Home
              break;
            case 1:
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => UserExplorePage()),
              );
              break;
            case 2:
              // Navigate to Notifications
              break;
          }
        },
      ),
    );
  }
}

class UserExplorePage extends StatelessWidget {
  final TextEditingController _categoryController = TextEditingController();
  final TextEditingController _subCategoryController = TextEditingController();

  UserExplorePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Explore'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(10.0),
        child: Column(
          children: <Widget>[
            Autocomplete<String>(
              optionsBuilder: (TextEditingValue textEditingValue) {
                if (textEditingValue.text == '') {
                  return const [];
                }
                return ['Medical', 'Law', 'Business'].where((option) => option
                    .toLowerCase()
                    .contains(textEditingValue.text.toLowerCase()));
              },
              onSelected: (String selection) {
                // Do something when a suggestion is selected
              },
              fieldViewBuilder: (BuildContext context,
                  TextEditingController textEditingController,
                  FocusNode focusNode,
                  VoidCallback onFieldSubmitted) {
                return TextField(
                  controller: textEditingController,
                  focusNode: focusNode,
                  decoration: const InputDecoration(
                    hintText: 'Enter a category',
                  ),
                );
              },
            ),
            Autocomplete<String>(
              optionsBuilder: (TextEditingValue textEditingValue) {
                if (textEditingValue.text == '') {
                  return const [];
                }
                return ['Dentist', 'Radiologist', 'Pathologist'].where(
                    (option) => option
                        .toLowerCase()
                        .contains(textEditingValue.text.toLowerCase()));
              },
              onSelected: (String selection) {
                // Do something when a suggestion is selected
              },
              fieldViewBuilder: (BuildContext context,
                  TextEditingController textEditingController,
                  FocusNode focusNode,
                  VoidCallback onFieldSubmitted) {
                return TextField(
                  controller: textEditingController,
                  focusNode: focusNode,
                  decoration: const InputDecoration(
                    hintText: 'Enter a sub-category',
                  ),
                );
              },
            ),

            ElevatedButton(
              child: const Text('Search'),
              onPressed: () {
                // Implement search functionality
              },
            ),
            // Add widgets for displaying search results
          ],
        ),
      ),
    );
  }
}
