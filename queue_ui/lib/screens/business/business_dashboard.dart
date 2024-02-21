import 'package:flutter/material.dart';

class DashboardPage extends StatelessWidget {
  const DashboardPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Container(
        width: MediaQuery.of(context).size.width * 0.1, // 10% of screen width
        height: MediaQuery.of(context).size.width * 0.05, // 5% of screen width
        child: Scaffold(
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
          body: ListView.builder(
            itemCount: 20, // Replace this with the length of your data list
            itemBuilder: (context, index) {
              return ListTile(
                leading: Text((index + 1).toString()), // Appointment number
                title: Text('Appointment Name'), // Appointment name
                trailing: PopupMenuButton(
                  itemBuilder: (context) => [
                    PopupMenuItem(
                      child: Text('Remove'),
                      value: 1,
                    ),
                    PopupMenuItem(
                      child: Text('Done'),
                      value: 2,
                    ),
                    PopupMenuItem(
                      child: Text('Re-call'),
                      value: 3,
                    ),
                  ],
                  onSelected: (value) {
                    // Handle menu option selection
                  },
                ),
              );
            },
          ),
          bottomNavigationBar: BottomNavigationBar(
            items: const <BottomNavigationBarItem>[
              BottomNavigationBarItem(
                icon: Icon(Icons.home),
                label: 'Dashboard',
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
                  // Navigate to Dashboard
                  break;
                case 1:
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => ExplorePage()),
                  );
                  break;
                case 2:
                  // Navigate to Notifications
                  break;
              }
            },
          ),
        ),
      ),
    );
  }
}

class ExplorePage extends StatelessWidget {
  final TextEditingController _categoryController = TextEditingController();
  final TextEditingController _subCategoryController = TextEditingController();

  ExplorePage({Key? key}) : super(key: key);

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
                return ['Medical', 'Law', 'Business']
                    .where((option) => option.contains(textEditingValue.text));
              },
              onSelected: (String selection) {
                // Do something when a suggestion is selected
              },
            ),
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
            ),
            ElevatedButton(
              child: const Text('Save'),
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
