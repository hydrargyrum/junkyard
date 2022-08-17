class RWLock {
	QMutex m_mutex;
	QWaitCondition m_evalCondition;
	int m_readers;
	int m_readersQueue;
	int m_writers;
	bool m_writing;

public:
	RWLock() : m_readers(0), m_readersQueue(0), m_writers(0), m_writing(false) {}

	void lockRead() {
		bool ticket = false;
		while (true) {
			m_mutex.lock();
			if (m_writers) {
				if (!ticket) {
					ticket = true;
					++m_readersQueue;
				}
				m_evalCondition.wait(&m_mutex);
			} else {
				if (ticket)
					--m_readersQueue;
				++m_readers;
				m_mutex.unlock();
				return;
			}
			m_mutex.unlock();
		}
	}

	void unlockRead() {
		m_mutex.lock();
		--m_readers;
		m_mutex.unlock();
		m_evalCondition.wakeAll();
	}

	void lockWrite() {
		bool ticket = false;
		while (true) {
			m_mutex.lock();
			if (!ticket) {
				ticket = true;
				++m_writers;
			}
			if (m_readers) {
				m_evalCondition.wait(&m_mutex);
			} else if (m_writing) {
				m_evalCondition.wait(&m_mutex);
			} else {
				m_writing = true;
				m_mutex.unlock();
				return;
			}
			m_mutex.unlock();
	}

	void unlockWrite() {
		m_mutex.lock();
		--m_writers;
		m_writing = false;
		m_mutex.unlock();
		m_evalCondition.wakeAll();
	}
};


/*
States
0 Nothing
0+r -> 1
0+w -> 2

1 Readers
1-r -> 1|0
1+r -> 1
1+w -> 3

2 Writer
2-w -> 0
2+r -> 5
2+w -> 4

3 WritersWaitingReaders
3-r -> 3|2|4
3+r -> 6
3+w -> 3

4 WritersWaitingWriter
4-w -> 4|2
4+r -> 7
4+w -> 4

5 ReadersWaitingWriter
5-w -> 1
5+r -> 5
5+w -> 7

6 ReadersWaitingWritersWaitingReaders
6-r -> 6|5|7
6+r -> 6
6+w -> 6

7 ReadersWaitingWritersWaitingWriter
7-w -> 7|5
7+r -> 7
7+w -> 7

*/
