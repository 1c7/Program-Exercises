input_file = ARGV[0]

# ����һ������ļ�ȫ�����ݵĺ���
def print_all(f)
  puts f.read()
  puts " "
end

# ����������ļ�ָ��ָ��ͷ
def rewind(f)
  f.seek(0, IO::SEEK_SET)
end

=begin
io.seek(offset,whence)

offsetӦ������ָ��λ��
whenceָ��Ӧ����ν���offset���ֵ
IO::SEEK_SET  ���ļ�ָ���ƶ���offset��ָ����λ�ô�
=end

def print_a_line(line_count, f)
  puts "#{line_count} #{f.readline()}"
end

current_file = File.open(input_file)

puts "���ȣ���������������ļ�����: "
puts # a blank line

# ʹ�������������ļ����ȫ����Ϣ
print_all(current_file)

puts "Now let's rewind, kind of like a tape."

# ���ļ�ָ���ƶ����ļ���ͷ
rewind(current_file)

puts "���3�� :"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# û�п��ƶ�ȡ���У����ǰ���˳��1��2��3�ж�ȡ��ֻ��ǰ�����һ���кŶ��ѡ�





