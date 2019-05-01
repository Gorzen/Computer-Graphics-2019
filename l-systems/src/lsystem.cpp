
#include "lsystem.h"
#include <stack>
#include <memory>
#include <iostream>
#include <math.h>

/*
Provided utilities:

- Dice class (utils/misc.h)
	Produces random values uniformly distributed between 0 and 1
	Example:
		Dice d;
		double random_val = d.roll();

- write_string_to_file (utils/misc.h)
	Write string data into a text file.
	Example:
		write_string_to_file("ala ma kota!", "ala.txt");
*/

std::string LindenmayerSystemDeterministic::expandSymbol(unsigned char const& sym) {
	/*============================================================
		TODO 1.1
		For a given symbol in the sequence, what should it be replaced with after expansion?
		The rules are in this->rules, see lsystem.h for details.
	*/

	auto search = (this->rules).find(sym);
  if (search != (this->rules).end()) {
      return search->second;
  } else {
      return std::string (1, sym);
  }

	/*
	You may find useful:
		map.find: Iterator to an element with key equivalent to key. If no such element is found, past-the-end (see end()) iterator is returned.
		http://en.cppreference.com/w/cpp/container/unordered_map/find
	============================================================
	*/
}

std::string LindenmayerSystem::expandOnce(std::string const& symbol_sequence) {
	/*============================================================
		TODO 1.2
		Perform one iteration of grammar expansion on `symbol_sequence`.
		Use the expandSymbol method
	*/
	std::string s;

	for(char c: symbol_sequence) {
		s += expandSymbol(c);
	}

	return s;
	//============================================================
}

std::string LindenmayerSystem::expand(std::string const& initial, uint32_t num_iters) {
	/*============================================================
		TODO 1.3
		Perform `num_iters` iterations of grammar expansion (use expandOnce)
	*/
	std::string s = initial;
	for(int i=0; i < num_iters; i++) {
		s = expandOnce(s);
	}

	return s;
	//============================================================
}

std::vector<Segment> LindenmayerSystem::draw(std::string const& symbols) {
	/*============================================================
		TODO 2.1
		Build line segments according to the sequence of symbols
		The initial position is (0, 0) and the initial direction is "up" (0, 1)
		Segment is std::pair<vec2, vec2>
	*/

	std::vector<Segment> list;
	vec2 p = vec2(0,0);
	vec2 p0;
	double d = 90;

  std::stack<vec2> sP;
  std::stack<double> sD;

	for(char c : symbols) {
		switch(c) {
			case '+':
				d += this->rotation_angle_deg;
        break;
      case '-':
				d -= this->rotation_angle_deg;
        break;
      case '[':
        sP.push(p);
        sD.push(d);
        break;
      case ']':
        if (!sP.empty() && !sD.empty()) { //Defensive programming :)
            p = sP.top();
            sP.pop();
            d = sD.top();
            sD.pop();
        }
        break;
			default:
				p0 = vec2(p);
				p += vec2(cos(d*M_PI/180), sin(d*M_PI/180));
        std::pair<vec2, vec2> segment (p0, p);
				list.push_back(segment);
        break;
		}
	}

	return list;

	//============================================================
}

std::string LindenmayerSystemStochastic::expandSymbol(unsigned char const& sym) {
	/*============================================================
		TODO 4.1
		For a given symbol in the sequence, what should it be replaced with after expansion?
		(stochastic case)
		The rules are in this->rules, but now these are stochastic rules because this method belongs to the LindenmayerSystemStochastic class, see lsystem.h for details.
	*/

	double prob = dice.roll();
	auto search = (this->rules).find(sym);
  if (search != (this->rules).end()) {
		double total = 0;
		for(StochasticRule sr : search->second) {
			if(sr.probability + total >= prob)
				return sr.expansion;
			else
				total += sr.probability;
		}
		std::cout << "probabilistic error" << std::endl; // Should never occur
		return std::string(1, sym);
  } else {
      return std::string (1, sym);
  }

	//============================================================
}

void LindenmayerSystemDeterministic::addRuleDeterministic(unsigned char sym, std::string const& expansion) {
	rules[sym] = expansion;
}

void LindenmayerSystemStochastic::addRuleStochastic(unsigned char sym, std::vector<StochasticRule> expansions_with_ps) {
	rules[sym] = expansions_with_ps;
}
