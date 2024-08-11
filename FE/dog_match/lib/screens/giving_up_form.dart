import 'package:dog_match/screens/my_dogs.dart';
import 'package:flutter/material.dart';

class GivingUpFormPage extends StatefulWidget {
  const GivingUpFormPage({super.key});

  @override
  State<GivingUpFormPage> createState() => _GivingUpFormPageState();
}

class _GivingUpFormPageState extends State<GivingUpFormPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Describe your dog"),
      ),
      body: Form(
        child: Padding(
          padding: const EdgeInsets.all(28.0),
          child: Column(
            children: [
              TextFormField(
                decoration:
                    InputDecoration(label: Text("what race is your dog?")),
              ),
              TextFormField(
                decoration: InputDecoration(label: Text("How old is it?")),
              ),
              ElevatedButton(
                  onPressed: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                          builder: (BuildContext context) =>
                              const MyDogsPage()),
                    );
                  },
                  child: Text("Add dog")),
            ],
          ),
        ),
      ),
    );
  }
}
