# ���} 16: �x���n��

filename = ARGV.first
script = $0

puts " ׼��������ݵ��ļ�����:#{filename}."
puts " ����㲻����ô�����밴�� CTRL-C (^C). "
puts " ���ȷ������밴�»س� "

print "? "
STDIN.gets

puts "���ڴ��ļ�..."
target = File.open(filename, 'w')

puts "�����������ļ�...�ټ�!"
target.truncate(1)

puts " ���������������� "

print "��һ��: "; line1 = STDIN.gets.chomp()
print "�ڶ���: "; line2 = STDIN.gets.chomp()
print "������: "; line3 = STDIN.gets.chomp()

puts "��׼������Щд���ļ���"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

puts " д����ϣ��ļ��رճɹ��� "
target.close()