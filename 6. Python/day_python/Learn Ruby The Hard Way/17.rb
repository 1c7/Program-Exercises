# ���} 17: ����ęn������
# �����������е�ʱ����Ҫ����2��������
# ��1�������� ׼�����Ƶ��ļ�������2�������� ׼��������Щ���ݵ��ļ�

from_file, to_file = ARGV
script = $0

indata = File.open(from_file).read()
  # ����indata���涼��׼�������ļ�������

puts " �������еĲ����ǰ� #{from_file} �����ݸ��Ƶ� #{to_file} ��ȥ "
puts "  ���»س�������, ����CTRL-C��ֹ. "
STDIN.gets
puts "----------------------------------------------------------------"

output = File.open(to_file, 'w')
output.write(indata)

puts "   ���鶼������..�ļ����ݸ��Ƴɹ�.. ����������~~~ "

output.close()
