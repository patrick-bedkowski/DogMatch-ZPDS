import 'package:dog_match/screens/main_screen.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        appBarTheme:
            AppBarTheme(backgroundColor: Color.fromARGB(255, 225, 201, 19)),
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
        primaryColor: Color.fromARGB(255, 225, 201, 19),
        scaffoldBackgroundColor: Color.fromARGB(255, 26, 22, 19),
        buttonTheme: ButtonThemeData(
            colorScheme: ColorScheme.fromSeed(seedColor: Colors.amber)),
        useMaterial3: true,
        textTheme: const TextTheme(
          // displayMedium: TextStyle(color: Color.fromARGB(255, 26, 22, 19)),
          labelSmall: TextStyle(color: Colors.white),
          bodyMedium: TextStyle(color: Colors.white),
        ),
      ),
      home: const MainScreenPage(title: 'Dog Match Home Page'),
    );
  }
}
