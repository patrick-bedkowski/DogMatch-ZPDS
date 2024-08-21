import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class radioInput<T> extends StatelessWidget {
  radioInput(
      {super.key,
      required this.values,
      required this.gruopValue,
      required this.labels,
      required this.onChange});

  final List<T> values;
  final T? gruopValue;
  final List<String> labels;
  void Function(T?) onChange;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        for (var i = 0; i < values.length; i++)
          Container(
            width: 100,
            child: Column(children: [
              Text(
                labels[i],
                style: TextStyle(
                    fontSize: 12,
                    color: Theme.of(context).textTheme.labelSmall!.color),
              ),
              SizedBox(
                height: 5,
              ),
              GestureDetector(
                onTap: () {
                  onChange(values[i]);
                },
                child: Container(
                  width: 24,
                  height: 24,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    color: gruopValue == values[i]
                        ? Theme.of(context).primaryColor
                        : Colors.white,
                    border: Border.all(
                      color: Colors.white,
                      width: 2,
                    ),
                  ),
                ),
              ),
            ]),
          ),
      ],
    );
  }
}
