import 'package:flutter/material.dart';

class TestScreenPage extends StatefulWidget {
  const TestScreenPage({super.key});

  @override
  State<TestScreenPage> createState() => _TestScreenPageState();
}

class _TestScreenPageState extends State<TestScreenPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        width: 200,
        height: 200,
        color: Colors.amber,
      ),
    );
  }
}
