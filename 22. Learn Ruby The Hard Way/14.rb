# ���} 14: ��ʾ�͂��f

user = ARGV.first    
#�����������ִ�е�ʱ�������ֺ��滹����һ��������������־���user��ֵ

prompt = '> '
#�����û���ʾ������ÿһ����ʾ����ĵط��������ǰͷ

puts "Hi #{user}, I'm the #{$0} script."

# #{$0} ������ļ�·�����ļ���, ����#{$1}��#{$2}û��Ӧ

puts "I'd like to ask you a few questions."
puts "Do you like me #{user}?"
print prompt
likes = STDIN.gets.chomp()

puts "Where do you live #{user}?"
print prompt
lives = STDIN.gets.chomp()

puts "What kind of computer do you have?"
print prompt
computer = STDIN.gets.chomp()

puts <<MESSAGE
Alright, so you said #{likes} about liking me.
You live in #{lives}.  Not sure where that is.
And you have a #{computer} computer.  Nice.
MESSAGE

=begin
ͬ�r���ע����ǣ��҂�Ҳ���� STDIN.gets ȡ���� gets��
�@���������Ж|���� ARGV �e���˜ʵ�gets���J�錢��һ���������ən�����Lԇ���e���x�|����
��Ҫ��ʹ���ߵ�ݔ�루��stdin���xȡ�Y�ϵ���r���҂�������_��ʹ�� STDIN.gets��
=end