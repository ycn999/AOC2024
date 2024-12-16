from itertools import combinations

def get_report(file_path):
    with open(file_path, 'r') as report_lines:
      report = []
      for lines in report_lines:
          levels = lines.replace('\n', '')
          report.append(levels)

      report_levels = []
      for r in report:
          report_levels.append([int(level) for level in r.split(' ')])

    return report_levels
reports = get_report(input_file_path)


def get_safe_reports(input):
  no_of_report = 0

  for report in reports:
    level_diff = []
    for i in range(1, len(report)):
      level_diff.append(report[i] - report[i-1])

    if (all([d > 0 for d in level_diff]) or all([d < 0 for d in level_diff])):
        if (all([abs(d) >= 1 and abs(d) <= 3 for d in level_diff])):
          no_of_report += 1

  return no_of_report


def get_safe_reports_dampen(input):
  no_of_report = 0

  for report in input:
    report_assess = 0
    for combi_drop in combinations(report, len(report)-1):
      level_diff = []
      for i in range(1, len(combi_drop)):
        level_diff.append(combi_drop[i] - combi_drop[i-1])

      for d in level_diff:
        if (all([d > 0 for d in level_diff]) or all([d < 0 for d in level_diff])):
            if (all([abs(d) >= 1 and abs(d) <= 3 for d in level_diff])):
              report_assess += 1
    
    if report_assess > 0:
       no_of_report += 1

  return no_of_report

puzzle1 = get_safe_reports(reports)
puzzle2 = get_safe_reports_dampen(reports)
