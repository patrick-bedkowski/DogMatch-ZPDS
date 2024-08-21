import 'package:flutter/material.dart';

class SliderInput extends StatelessWidget {
  SliderInput({super.key, required this.currentValue, required this.onChange});

  double currentValue;
  void Function(double) onChange;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Text(
          "sliiide",
          style:
              TextStyle(color: Theme.of(context).textTheme.labelSmall!.color),
        ),
        Slider(
          value: currentValue,
          max: 100,
          divisions: 5,
          label: currentValue.round().toString(),
          onChanged: onChange,
        ),
      ],
    );
  }
}
