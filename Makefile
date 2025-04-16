
CC = clang++
CFLAGS = -Wall -Wextra -g
TARGET = hello

SRCS = test.c test2.cpp
OBJS = test.o test2.o

$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) $(OBJS) -o $(TARGET)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

%.o: %.cpp
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(TARGET) $(OBJS)
