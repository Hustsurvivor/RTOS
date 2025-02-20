with open('data/imdb-test/sql.txt')as f:
    sql_lines = f.readlines()
    qid2sql_line = { line.split('#####')[0]:line.split('#####')[1] for line in sql_lines}
    
with open('data/imdb-test/seq.txt')as f:
    seq_lines = f.readlines()
    qid2seq_line = { line.split('#####')[0]:line.split('#####')[1] for line in seq_lines}
    
with open('data/imdb-test/plan.txt')as f:
    plan_lines = f.readlines()
    qid2plan_line = { line.split('#####')[0]:line.split('#####')[1] for line in plan_lines}

with open('data/imdb-test/time.txt')as f:
    time_lines = f.readlines()
    qid2time_line = { line.split('#####')[0]:line.split('#####')[1] for line in time_lines}

new_lines = []
new_sql_lines = [ qid + '#####' + qid2sql_line[qid].strip() + '\n' for qid in list(qid2seq_line.keys())[:100]]
new_seq_lines = [ qid + '#####' + qid2seq_line[qid].strip() + '\n' for qid in list(qid2seq_line.keys())[:100]]
new_plan_lines = [ qid + '#####' + qid2plan_line[qid].strip() + '\n' for qid in list(qid2seq_line.keys())[:100]]
new_time_lines = [ qid + '#####' + qid2time_line[qid].strip() + '\n' for qid in list(qid2seq_line.keys())[:100]]

with open('data/imdb-test/sql.txt', 'w')as f:
    f.writelines(new_sql_lines)
    
with open('data/imdb-test/seq.txt', 'w')as f:
    f.writelines(new_seq_lines)
    
with open('data/imdb-test/plan.txt', 'w')as f:
    f.writelines(new_plan_lines)

with open('data/imdb-test/time.txt', 'w')as f:
    f.writelines(new_time_lines)