import 'package:dog_match/screens/recommended_dogs.dart';
import 'package:flutter/material.dart';

class LookingFormPage extends StatefulWidget {
  const LookingFormPage({super.key});

  @override
  State<LookingFormPage> createState() => _LookingFormPageState();
}

class _LookingFormPageState extends State<LookingFormPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Enter your preferences"),
      ),
      body: Form(
        child: Padding(
          padding: const EdgeInsets.all(28.0),
          child: Column(
            children: [
              TextFormField(
                decoration: InputDecoration(
                    label: Text("what dog are you looking for?")),
              ),
              TextFormField(
                decoration:
                    InputDecoration(label: Text("How much time do you have?")),
              ),
              Row(
                children: [
                  ElevatedButton(
                      onPressed: () {
                        Navigator.of(context).push(
                          MaterialPageRoute(
                              builder: (BuildContext context) =>
                                  const RecommendedDogsPage()),
                        );
                      },
                      child: Text("Show races")),
                  ElevatedButton(
                      onPressed: () {
                        Navigator.of(context).push(
                          MaterialPageRoute(
                              builder: (BuildContext context) =>
                                  const RecommendedDogsPage()),
                        );
                      },
                      child: Text("Show dogs")),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
