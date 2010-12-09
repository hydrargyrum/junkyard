template <typename T>
class _dat_ptr {
	T *m_ptr;
	int m_strongs;
	int m_weaks;
	
public:
	_dat_ptr(T *ptr) : m_ptr(ptr), m_strongs(0), m_weaks(0) {}
	~_dat_ptr() { delete m_ptr; }
	
	void weakRef() { m_weaks++; }
	void weakDeref() { m_weaks--; testDelete(); }
	void strongRef() { m_strongs++; }
	void strongDeref() { m_strongs--; testDelete(); }
	bool isValid() const { return (m_ptr != 0); }
	T *get() const { return m_ptr; }

private:
	void testDelete() {
		if (!m_strongs) {
			delete m_ptr;
			m_ptr = 0;
			if (!m_weaks)
				delete this;
		}
	}
	_dat_ptr(const _dat_ptr&);
	_dat_ptr& operator=(const _dat_ptr&);
};

template <typename T>
class weak_ptr {
	friend class strong_ptr<T>;
	
	_dat_ptr<T> *m_data;
	
	weak_ptr(_dat_ptr<T> *data) : m_data(data) {
		if (m_data)
			m_data.weakRef();
	}
public:
	weak_ptr() : m_data(0) {}
	weak_ptr(const weak_ptr<T> &other) : m_data(other.m_data) {
		if (m_data)
			m_data->weakRef();
	}
	~weak_ptr() {
		clear();
	}
	weak_ptr<T> &operator=(const weak_ptr<T> &other) {
		weak_ptr<T> copy(other);
		this->swap(copy);
		return *this;
	}
	
	void clear() {
		if (m_data) {
			m_data->weakDeref();
			m_data = 0;
		}
	}
	
	strong_ptr<T> toStrong() {
		if (!*this)
			return strong_ptr<T>();
		return strong_ptr<T>(m_data);
	}
	operator bool() const {
		return (m_data && m_data->isValid());
	}
	
	void swap(weak_ptr<T> &other) {
		std::swap(m_data, other.m_data);
	}
};

template <typename T>
class strong_ptr {
	_dat_ptr<T> *m_data;
	
	friend class weak_ptr<T>;
	
	strong_ptr(_dat_ptr<T> *data) : m_data(data) {
		if (m_data)
			data->strongRef();
	}
public:
	strong_ptr(T *ptr = 0) : m_data(0) {
		if (ptr) {
			m_data = new _dat_ptr(ptr);
			m_data->strongRef();
		}
	}
	strong_ptr(const strong_ptr<T> &other) : m_data(other.data) {
		if (m_data)
			m_data->strongRef();
	}
	strong_ptr<T> &operator=(const strong_ptr<T> &other) {
		strong_ptr<T> copy(other);
		this->swap(copy);
		return *this;
	}
	~strong_ptr() {
		clear();
	}
	
	void clear() {
		if (m_data) {
			m_data->strongDeref();
			m_data = 0;
		}
	}
	
	T *get() const {
		if (!*this)
			return 0;
		return m_data->get();
	}
	operator bool() const {
		return (m_data && m_data->isValid());
	}
	weak_ptr<T> toWeak() {
		if (!*this)
			return weak_ptr<T>();
		return weak_ptr<T>(m_data);
	}
	void swap(strong_ptr<T> &other) {
		std::swap(m_data, other.m_data);
	}
};
