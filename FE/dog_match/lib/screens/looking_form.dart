import 'package:dog_match/screens/recommended_dogs.dart';
import 'package:dog_match/utils/widgets/primary_button.dart';
import 'package:dog_match/utils/widgets/radio_input.dart';
import 'package:dog_match/utils/widgets/slider.dart';
import 'package:dog_match/utils/widgets/text_input.dart';
import 'package:flutter/material.dart';

class LookingFormPage extends StatefulWidget {
  LookingFormPage({super.key});

  @override
  State<LookingFormPage> createState() => _LookingFormPageState();
}

enum time { low, medium, high }

class _LookingFormPageState extends State<LookingFormPage> {
  final labels = ["0.5 - 1h", "1 - 2h", "2+h"];
  final timeValues = [time.low, time.medium, time.high];
  time? selectedTime = time.low;
  String _enteredText = "";
  double _currentSliderValue = 20;

  final _formKey = GlobalKey<FormState>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Dog Match"),
        automaticallyImplyLeading: false,
      ),
      body: Form(
        key: _formKey,
        child: Padding(
          padding: const EdgeInsets.all(28.0),
          child: Container(
            width: 300,
            child: Column(
              children: [
                TextInput(
                  onSave: (val) {
                    setState(() {
                      _enteredText = val!;
                    });
                  },
                  validate: (value) {
                    if (value == null ||
                        value.isEmpty ||
                        value.trim().length <= 1 ||
                        value.trim().length > 50) {
                      return "Must be between 1 and 50 characters";
                    }
                    return null;
                  },
                ),
                SizedBox(
                  height: 30,
                ),
                radioInput<time>(
                    values: timeValues,
                    gruopValue: selectedTime,
                    labels: labels,
                    onChange: (val) {
                      setState(() {
                        selectedTime = val;
                      });
                    }),
                SizedBox(
                  height: 30,
                ),
                SizedBox(
                  height: 10,
                ),
                SliderInput(
                    currentValue: _currentSliderValue,
                    onChange: (double value) {
                      setState(() {
                        _currentSliderValue = value;
                      });
                    }),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceAround,
                  children: [
                    primaryButton(
                      text: "Show races",
                      onPress: () {
                        if (_formKey.currentState!.validate()) {
                          Navigator.of(context).push(
                            MaterialPageRoute(
                                builder: (BuildContext context) =>
                                    const RecommendedDogsPage()),
                          );
                        }
                      },
                    ),
                    primaryButton(
                      text: "Show dogs",
                      onPress: () {
                        if (_formKey.currentState!.validate()) {
                          Navigator.of(context).push(
                            MaterialPageRoute(
                                builder: (BuildContext context) =>
                                    const RecommendedDogsPage()),
                          );
                        }
                      },
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
