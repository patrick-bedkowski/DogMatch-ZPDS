import 'package:flutter/material.dart';

class primaryButton extends StatelessWidget {
  primaryButton({super.key, required this.text, required this.onPress});

  String text;
  void Function() onPress;

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
        onPressed: onPress,
        style: ElevatedButton.styleFrom(
            backgroundColor: Theme.of(context).primaryColor),
        child: const Padding(
          padding: EdgeInsets.symmetric(horizontal: 8.0, vertical: 10.0),
          child: Text(
            "Show races",
            style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
          ),
        ));
  }
}
