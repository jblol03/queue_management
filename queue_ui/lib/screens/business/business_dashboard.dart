import 'package:flutter/material.dart';
import 'package:multi_select_flutter/multi_select_flutter.dart';

class DashboardPage extends StatelessWidget {
  const DashboardPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: SizedBox(
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
                title: const Text('Jay Billimoria'), // Appointment name
                trailing: PopupMenuButton(
                  itemBuilder: (context) => [
                    const PopupMenuItem(
                      value: 1,
                      child: Text('Remove'),
                    ),
                    const PopupMenuItem(
                      value: 2,
                      child: Text('Done'),
                    ),
                    const PopupMenuItem(
                      value: 3,
                      child: Text('Re-call'),
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
  final TextEditingController _companyController = TextEditingController();

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
                    hintText: 'Category',
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
                    hintText: 'Sub-category',
                  ),
                );
              },
            ),
            TextField(
              controller: _companyController,
              decoration: const InputDecoration(
                hintText: 'Company Name',
              ),
            ),
            ElevatedButton(
              child: const Text('Save'),
              onPressed: () {
                // Implement savw functionality
              },
            ),
            Divider(
              color: Colors.grey,
              height: 30,
              thickness: 1,
            ),
            MultiSelectDialogField(
              items: [
                'Monday',
                'Tuesday',
                'Wednesday',
                'Thursday',
                'Friday',
                'Saturday',
                'Sunday'
              ].map((day) => MultiSelectItem<String>(day, day)).toList(),
              title: Text("Select Days"),
              selectedColor: Colors.blue,
              onConfirm: (values) {
                // Handle the selected values
              },
            ),

            TextField(
              decoration: InputDecoration(
                labelText: "Slots",
              ),
            ),

            ElevatedButton(
              child: const Text('Add Appointment'),
              onPressed: () {
                // Implement add appointment functionality
              },
            ),
            // Add widgets for displaying search results
          ],
        ),
      ),
    );
  }
}
