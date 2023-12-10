from collections import defaultdict
import sys
import concurrent.futures
import os
import multiprocessing

def parse_input_data(lines):
    almanac = defaultdict(list)
    seeds = list()
    capture_key = None
    capture_idx = -1

    for line in lines:
        if not line:
            capture_key = False
            continue
        elif "seeds:" in line:
            seeds = list(map(int, line.split(": ")[1].split(" ")))
        elif "map" in line:
            capture_key = line.split(" ")[0]
            capture_idx += 1
        else:
            values = list(map(int, line.split(" ")))
            almanac[capture_idx].append(values)
    
    return (seeds, almanac)

filename = "input.txt"
with open(filename, 'r') as f: lines = f.read().splitlines()
seeds, almanac = parse_input_data(lines)

# def get_dest_loc(entries, tracking):
    # for entry in entries:
    #     dest, source, range = entry
    #     if source <= tracking <= source+range:
    #         tracking = (tracking-source)+dest
    #         return tracking
    # return tracking


def run_through_almanac(init_seed, rng):
    location = sys.maxsize

    for seed in range(init_seed, init_seed+rng):
        tracking = seed
        num_steps = len(almanac.keys())

        # print(seed)

        for step in range(num_steps):
            for entry in almanac[step]:
                dest, source, rng = entry
                if source <= tracking < source+rng:
                    # print(step, entry, tracking)
                    tracking = (tracking-source)+dest
                    break

        location = min(location, tracking)           

    return location


def seed_gen(init_seed, seed_range):
    for seed in range(init_seed, init_seed+seed_range):
        yield seed


if __name__ == "__main__":
    location = sys.maxsize
    
    tasks = [(seed, rng) for seed, rng in zip(seeds[::2], seeds[1::2])]
    logger = 1

    for task in tasks:
        location = min(location, run_through_almanac(*task))
    
    print(location)

    # with concurrent.futures.ProcessPoolExecutor() as executor:
    #     results = executor.map(run_through_almanac, seeds)

    #     for result in results:
    #         location = min(location, result)


'''

104070863 - too high. That means my division of work is now accurate. 


def run_through_almanac(arguments):

    init_seed, rng, almanac = arguments
    # print(f"proc id: {os.getpid()}")
    # print(init_seed, range)

    # locations = []
    location = sys.maxsize

    for seed in range(init_seed, init_seed+rng):
    
        tracking = seed

        # find the soil
        entries = almanac["seed-to-soil"]
        tracking = get_dest_loc(entries, tracking)

        # find the fert
        entries = almanac["soil-to-fertilizer"]
        tracking = get_dest_loc(entries, tracking)

        # find the water
        entries = almanac["fertilizer-to-water"]
        tracking = get_dest_loc(entries, tracking)

        # find the light
        entries = almanac["water-to-light"]
        tracking = get_dest_loc(entries, tracking)

        # find the temperature
        entries = almanac["light-to-temperature"]
        tracking = get_dest_loc(entries, tracking)

        # find the humidity
        entries = almanac["temperature-to-humidity"]
        tracking = get_dest_loc(entries, tracking)

        # find the location
        entries = almanac["humidity-to-location"]
        tracking = get_dest_loc(entries, tracking)

        # locations.append(tracking)
        if not location:
            location = tracking
        else:
            location = min(location, tracking)
    
    return location


Tried and failed. 



    # num_processes = 61
    # # data_collected = Queue()
    # processes = []
    # for init_seed, sr in new_seeds:
    #     with multiprocessing.Pool(processes=num_processes) as pool:
    #         print(f'Input range#{logger} has started {init_seed}, {sr}')
    #         logger += 1
    #         locations = pool.starmap(run_through_almanac, [(seed, almanac) \
    #                                                        for seed in seed_gen(init_seed, sr)])
            
    #         location = min(location, min(locations))





    # trying asyncio to parralellize the problem. 
    executor = ProcessPoolExecutor(max_workers=61)

    for init_seed, sr in new_seeds:
        print(f"[+] Running range index {logger}")
        logger += 1
        data = await asyncio.gather(*(loop.run_in_executor(executor, run_through_almanac, seed, almanac) \
                                  for seed in range(init_seed, init_seed+sr)))

        location = min(location, min(data))

    print(location)
    # pool = multiprocessing.Pool(processes=60)
    # sr = seed_range
    # for init_seed, sr in new_seeds:
    #     print(f'[+]PID {os.getpid()}: Input range#{logger} has started {init_seed}, {sr}')
    #     logger += 1
    #     # locations = pool.starmap(run_through_almanac, [(seed, almanac) \
    #     #                                                for seed in seed_gen(init_seed, sr)])
    #     locations.append(pool.apply_async(run_through_almanac, (seed_gen(init_seed, sr), almanac)))
    
    # pool.close()
    # pool.join()
    # print(min(locations))

    # for seed in seeds:
    #     location = min(location, run_through_almanac(seed, almanac))

    # print(location)

'''