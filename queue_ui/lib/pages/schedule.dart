import 'package:flutter/material.dart';

class Schedule extends StatefulWidget {
  const Schedule({Key? key}) : super(key: key);

  @override
  _ScheduleState createState() => _ScheduleState();
}

class _ScheduleState extends State<Schedule> {
  final weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
  ];
  List<bool> isSelected = List.generate(7, (index) => false);
  final _shiftNameController = TextEditingController();
  TimeOfDay? _selectedStartTime;
  TimeOfDay? _selectedEndTime;
  final _slotController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Schedule")),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Wrap(
              spacing: 5.0,
              runSpacing: 3.0,
              children: List<Widget>.generate(
                7,
                (int index) {
                  return FilterChip(
                    label: Text(weekdays[index]),
                    selected: isSelected[index],
                    onSelected: (bool selected) {
                      setState(() {
                        isSelected[index] = selected;
                      });
                    },
                  );
                },
              ).toList(),
            ),
            const SizedBox(height: 16),
            Text("Create Shift",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            TextField(
              controller: _shiftNameController,
              decoration: InputDecoration(labelText: 'Shift Name'),
            ),
            ListTile(
              title: Text(_selectedStartTime == null
                  ? 'Select Start Time'
                  : _selectedStartTime!.format(context)),
              trailing: Icon(Icons.keyboard_arrow_down),
              onTap: () async {
                final selectedTime = await showTimePicker(
                  context: context,
                  initialTime: _selectedStartTime ?? TimeOfDay.now(),
                );
                if (selectedTime != null) {
                  setState(() {
                    _selectedStartTime = selectedTime;
                  });
                }
              },
            ),
            ListTile(
              title: Text(_selectedEndTime == null
                  ? 'Select End Time'
                  : _selectedEndTime!.format(context)),
              trailing: Icon(Icons.keyboard_arrow_down),
              onTap: () async {
                final selectedTime = await showTimePicker(
                  context: context,
                  initialTime: _selectedEndTime ?? TimeOfDay.now(),
                );
                if (selectedTime != null) {
                  setState(() {
                    _selectedEndTime = selectedTime;
                  });
                }
              },
            ),
            ElevatedButton(
              onPressed: () {},
              child: Text('Create Shift'),
            ),
            SizedBox(height: 16),
            Text("Create Slot",
                style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold)),
            DropdownButton<String>(
              hint: Text('Select Shift'),
              items:
                  <String>['Shift 1', 'Shift 2', 'Shift 3'].map((String value) {
                return DropdownMenuItem<String>(
                  value: value,
                  child: Text(value),
                );
              }).toList(),
              onChanged: (_) {},
            ),
            TextField(
              controller: _slotController,
              decoration: InputDecoration(labelText: 'Number of Slots'),
              keyboardType: TextInputType.number,
            ),
            ElevatedButton(
              onPressed: () {},
              child: Text('Create Slot'),
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        child: Icon(Icons.add),
      ),
    );
  }
}
