DATE = 23
START_HOUR = 9
END_HOUR = 17

# Start time of each lab session
time_ints = [930, 1030, 1130, 1230, 1330, 1430, 1530, 1630]

# Check that the timestamp is on DATE and between START_HOUR and END_HOUR
def is_valid_timestamp(times) :
  if (int(times[0]) != 23) :
    return False
  return (9 <= int(times[1])) and (int(times[1]) <= 17)

# Parse the records
def parse_records() :
  # Read from the csv
  name = raw_input('Input file (csv): ')
  f1 = open(name, 'r')
  data = [line[:-1] for line in f1.readlines()]
  f1.close();

  records = dict()
  for entry in data :
    fields = entry.split(',')
    uid = fields[0]
    timestamp = fields[2]
    times = timestamp.split(":")

    if not(is_valid_timestamp(times)) :
      continue

    if (uid not in records.keys()) :
      records[uid] = dict()
      records[uid]["is_in"] = []
      records[uid]["insert"] = []
      records[uid]["delete"] = []
      records[uid]["misc"] = []
      records[uid]["time_int"] = int(times[1]) - START_HOUR \
                                 if int(times[2]) > 30 \
                                 else int(times[1]) - (START_HOUR + 1)
    else :
      # Only record the entry if the timestamp is in the correct time interval
      hm = times[1] + times[2]
      if not(time_ints[records[uid]["time_int"]] <= int(hm)
             and int(hm) < (time_ints[records[uid]["time_int"]] + 100)) :
        continue

    if (len(fields) > 7) :
      comp1 = float(fields[6])
      comp2 = float(fields[7])
      comp3 = float(fields[8]) if len(fields) > 8 else -1

      record = dict()
      record["timestamp"] = timestamp

      if (comp3 > 0) :
        # This entry is an attempt for delete
        record["bit_vector"] = fields[5]
        record["complexity"] = comp3
        records[uid]["delete"].append(record)
      elif (comp2 > 0) :
        # This entry is an attempt for insert
        record["bit_vector"] = fields[4]
        record["complexity"] = comp2
        records[uid]["insert"].append(record)
      elif (comp1 > 0) :
        # This entry is an attempt for is_in
        record["bit_vector"] = fields[3]
        record["complexity"] = comp1
        records[uid]["is_in"].append(record)
      else :
        # Miscellaneous entries
        record["bit_vectors"] = [fields[3], fields[4], fields[5]]
        record["complexities"] = [fields[6], fields[7], fields[8]]
        records[uid]["misc"].append(record)

  return records
